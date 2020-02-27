FROM quay.io/operator-framework/ansible-operator:v0.14.1

COPY watches.yaml ${HOME}/watches.yaml

COPY roles/ ${HOME}/roles/

COPY watches.yaml ${HOME}/watches.yaml

COPY roles/ ${HOME}/roles/

USER root

RUN yum -y install openssh-clients sudo procps-ng

RUN useradd --home-dir /opt/ansible --no-create-home --uid 1001 --gid 0 --shell /sbin/nologin  ansible-operator

RUN echo "ansible-operator ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/99-operator

USER 1001
