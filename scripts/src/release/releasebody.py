import sys

sys.path.append('./scripts/src/')
from release import releasechecker
from utils import utils

def make_release_body(version, image_name, release_info):
    body = f"Chart verifier version {version} <br><br>Docker Image:<br>- {image_name}:{version}<br><br>"
    body += "This version includes:<br>"
    for info in release_info:
        if info.startswith("<"):
            body += info
        else:
            body += f"- {info}<br>"

    print(f"[INFO] Release body: {body}")
    utils.add_output("PR_release_body",body)

def main():
    version_info = releasechecker.get_version_info()
    make_release_body(version_info["version"],version_info["quay-image"],version_info["release-info"])
    # tarfile = create(args.release)
    # print(f'[INFO] Verifier tarball created : {tarfile}.')
    # utils.add_output("tarball_full_name",tarfile)

