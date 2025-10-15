NODE_TLS_REJECT_UNAUTHORIZED=0 npm install

npm config set strict-ssl false

git config --global user.name "Ashish"
git config --global user.email "ashishvista@gmail.com"


const lpm = require("lp-messaging-sdk");

const proxy = {
  host: 'yourHost.com',
  port: 8080,
  protocol: 'http',
  path: 'user/1',
  auth: {
    username: 'username',
    password: 'password',
  }
};

lpm.configureProxy(proxy);

const connection = lpm.createConnection({
  appId: 'quick_start',
  accountId: '12345678',
  userType: lpm.UserType.BRAND,
});