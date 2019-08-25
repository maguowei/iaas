cat <<'EOF' > execute.txt
${{BODY_CONTENT}}
EOF
sed -i 's/\r//g' execute.txt
echo '#!/bin/sh -l' > execute.sh
python3 code.py >> execute.sh
shellcheck execute.sh
bash -e execute.sh