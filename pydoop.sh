#!/bin/bash
PYDOOP_INSTALL_SCRIPT=$(cat <<EOF
#!/bin/bash
NM_PID=/var/run/hadoop-yarn/yarn-yarn-nodemanager.pid
RM_PID=/var/run/hadoop-yarn/yarn-yarn-resourcemanager.pid
while [ ! -f \${RM_PID} ] && [ ! -f \${NM_PID} ]; do
  sleep 2
done
export JAVA_HOME=/etc/alternatives/java_sdk
sudo -E pip install pydoop
EOF
)
echo "${PYDOOP_INSTALL_SCRIPT}" | tee -a /tmp/pydoop_install.sh
chmod u+x /tmp/pydoop_install.sh
/tmp/pydoop_install.sh >/tmp/pydoop_install.out 2>/tmp/pydoop_install.err &