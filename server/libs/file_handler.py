import os
import secrets

from werkzeug.utils import secure_filename
from config import Configs

ALLOWED_EXTENSIONS = {"gcode"}


class FileHandler:
    @classmethod
    def allowed_file(cls, filename: str) -> bool:
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

    @classmethod
    def random_name_gen(cls, filename) -> str:
        secure_name = secure_filename(filename)
        extension = secure_name.rsplit(".", 1)[1]
        random_name = secrets.token_hex(16)
        fullname = random_name + "." + extension
        return fullname

    @classmethod
    def save_file(cls, file, filename: str) -> None:
        file.save(os.path.join(Configs.UPLOAD_FOLDER, filename))
