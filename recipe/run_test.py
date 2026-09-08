import os
import re
import subprocess
from datetime import datetime


version = datetime.strptime(os.environ["PKG_VERSION"], "%Y.%m.%d.%H.%M.%S")
release_tag = version.strftime("RELEASE.%Y-%m-%dT%H-%M-%SZ")
output = subprocess.check_output(["minio", "--version"], text=True)
print(output, end="")

assert re.search(
    rf"^minio version {re.escape(release_tag)} \(commit-id=[0-9a-f]{{40}}\)$",
    output,
    re.MULTILINE,
), "MinIO must report the packaged release and its Git commit"
