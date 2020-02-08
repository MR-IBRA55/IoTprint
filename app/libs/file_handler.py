import os
import secrets

from config import Configs

ALLOWED_EXTENSIONS = {"gcode"}


class FileHandler:
    @classmethod
    def allowed_file(cls, filename: str) -> bool:
        return (
                "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

    @classmethod
    def save_file(cls, file) -> str:
        random_name = secrets.token_hex(16)
        file.save(os.path.join(Configs.UPLOAD_FOLDER, random_name + ".gcode"))
        return random_name
