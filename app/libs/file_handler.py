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
    def random_name_gen(cls) -> str:
        return secrets.token_hex(16) + ".gcode"

    @classmethod
    def save_file(cls, file, filename: str) -> None:
        file.save(os.path.join(Configs.UPLOAD_FOLDER, filename))
