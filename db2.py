ssh-keygen -t ed25519 -C "org1_key" -f ~/.ssh/id_ed25519_org1


Example ~/.ssh/config (Final Version)
Host *
    AddKeysToAgent yes
    UseKeychain yes

Host gitlab-org1
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_ed25519_org1

Host gitlab-org2
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_ed25519_org2