# Configuration GitHub Actions

## Secrets requis

Pour que le workflow fonctionne, vous devez configurer les secrets suivants dans votre repository GitHub :

1. **DOCKERHUB_USERNAME** : Votre nom d'utilisateur DockerHub
2. **DOCKERHUB_TOKEN** : Votre token d'accès DockerHub (pas votre mot de passe)

### Comment configurer les secrets :

1. Allez dans votre repository GitHub
2. Cliquez sur **Settings** → **Secrets and variables** → **Actions**
3. Cliquez sur **New repository secret**
4. Ajoutez les deux secrets :
   - `DOCKERHUB_USERNAME` : votre username DockerHub
   - `DOCKERHUB_TOKEN` : votre token (généré dans DockerHub → Account Settings → Security)

### Comment générer un token DockerHub :

1. Connectez-vous à DockerHub
2. Allez dans **Account Settings** → **Security**
3. Cliquez sur **New Access Token**
4. Donnez un nom au token et copiez-le (vous ne pourrez le voir qu'une seule fois)

