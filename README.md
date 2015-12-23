## How to create an rpm to deploy arbitrary files

In this example we'll deploy repo files in _/etc/yum.repos.d/_ :

- Install [this excellent docker rpm builder](https://github.com/alanfranz/docker-rpm-builder)

- Place the desired repo files in the _repos-0.0.1_ folder

- Edit the _repos.spec_ file to include all the files you need

- run:

```
$ tar zcvf repos.tar.gz repos-0.0.1/* ; docker-rpm-builder dir alanfranz/drb-epel-7-x86-64:latest . .
```
 
- The result rpm will be store in the x86_64 folder; use:

```
$ yum install -y x86_64/repos-0.0.1-1.el7.centos.x86_64.rpm
```

This can be easily extended at will to deploy arbitrary files in arbitrary positions on the filesystem.
