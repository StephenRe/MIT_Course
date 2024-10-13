import os
import sys
import docker

client = docker.from_env()

runningcontainers = []
allcontainers = []
my_containers = [
    'some-mysql',
    'some-mongo',
    'some-redis',
    'some-cassandra'
]
print(f'my containers:', my_containers)

containers = client.containers.list(all=True)
for container in containers:
    allcontainers.append(container.name)
print('available containers:', allcontainers)

containers = client.containers.list()
for container in containers:
    runningcontainers.append(container.name)
print('running containers:', runningcontainers)

def create(cmd, db):
    result = os.system(cmd)
    if result == 0:
        print(f'created {db}')

def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

argument = len(sys.argv)
if argument > 1:
    argument = sys.argv[1]

if argument == '-delete':
    for deleting in my_containers:
        delete(deleting)

if argument == '-create':
    if 'some-mysql' in allcontainers:
        print('container some-mysql already created')
    else:
        create('docker run -p 3300:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')

    if 'some-mongo' in allcontainers:
        print('container some-mongo already created')
    else:
        create("docker run -p 27017:27017 --name some-mongo -d mongo", 'mongo')

    if 'some-redis' in allcontainers:
        print('container some-redis already created')
    else:
        create("docker run -p 6379:6379 --name some-redis -d redis", 'redis')
    
    if 'some-cassandra' in allcontainers:
        print('container some-cassandra already created')
    else:
        create("docker run -p 9042:9042 --name some-cassandra -d cassandra", 'cassandra')

if argument == '-start':
    for starting in my_containers:
        if starting in runningcontainers:
            print(f'{starting} container already running')
        elif 'some-mysql' in allcontainers and 'some-mysql' not in runningcontainers:
            os.system(f'docker start {starting}')
            print(f'{starting} container started')

if argument == '-stop':
    for running in runningcontainers:
        container = client.containers.get(running)
        container.stop()
        print(f'container {running} stopped')
    print('all containers stopped')


       





