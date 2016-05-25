from fabric.api import local, env

def build():
    local("docker build -t hello-world-core .")
