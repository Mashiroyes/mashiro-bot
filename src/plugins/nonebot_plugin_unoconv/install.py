import sys
import subprocess

def linux_install(pkg):
    try:
        if sys.platform.startswith('linux'):
            if not subprocess.call(["command", "-v", pkg], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
                
                if subprocess.call(["command", "-v", "yum"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
                    print("Redhat based system, using yum to install package")
                    subprocess.call(["sudo", "yum", "-y", "install", pkg])
                    
                elif subprocess.call(["command", "-v", "apt-get"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
                    print("Debian based system, using apt-get to install package")
                    subprocess.call(["sudo", "apt-get", "update"])
                    subprocess.call(["sudo", "apt-get", "install", pkg])
                    
                else:
                    print('Unknown package manager, exiting...')
                
        else:
            print('Not a Linux system, exiting...')
            
    except Exception as e:
        print('unoconv安装失败, 请尝试手动安装')
            
if __name__ == "__main__":
    linux_install("unoconv")
