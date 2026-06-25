from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import time

app = Flask(__name__)

mp_face = mp.solutions.face_mesh
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

face_mesh = mp_face.FaceMesh(max_num_faces=1, refine_landmarks=True)
pose = mp_pose.Pose()

camera = cv2.VideoCapture(0)
inicio = time.time()


def gerar_frames():
    while True:
        sucesso, frame = camera.read()

        if not sucesso:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_result = face_mesh.process(rgb)
        pose_result = pose.process(rgb)

        olhar = "Nao detectado"
        postura = "Nao detectada"
        enquadramento = "Nao detectado"
        articulacoes = "Nao detectadas"
        score = 60

        if face_result.multi_face_landmarks:
            face = face_result.multi_face_landmarks[0]
            nariz = face.landmark[1]

            if 0.35 < nariz.x < 0.65:
                olhar = "Olhando para camera"
                score += 15
            else:
                olhar = "Olhar desviado"
                score -= 10

            if 0.25 < nariz.x < 0.75:
                enquadramento = "Centralizado"
                score += 10
            else:
                enquadramento = "Fora do centro"
                score -= 10

            mp_draw.draw_landmarks(
                frame,
                face,
                mp_face.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_draw.DrawingSpec(thickness=1, circle_radius=1)
            )

        if pose_result.pose_landmarks:
            lm = pose_result.pose_landmarks.landmark

            ombro_esq = lm[11]
            ombro_dir = lm[12]

            diferenca_ombros = abs(ombro_esq.y - ombro_dir.y)

            if diferenca_ombros < 0.05:
                postura = "Adequada"
                score += 15
            else:
                postura = "Ombros desalinhados"
                score -= 10

            articulacoes = "Detectadas"

            mp_draw.draw_landmarks(
                frame,
                pose_result.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        score = max(0, min(100, score))
        tempo = int(time.time() - inicio)

        cv2.rectangle(frame, (10, 10), (670, 210), (0, 0, 0), -1)

        cv2.putText(frame, "Presenter Vision AI", (25, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        cv2.putText(frame, f"Olhar: {olhar}", (25, 85),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        cv2.putText(frame, f"Postura: {postura}", (25, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        cv2.putText(frame, f"Enquadramento: {enquadramento}", (25, 155),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        cv2.putText(frame, f"Articulacoes: {articulacoes} | Score: {score}/100 | Tempo: {tempo}s",
                    (25, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
        )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(
        gerar_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)