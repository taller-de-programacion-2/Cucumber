
module.exports = {
    NODE_ENV: process.env.NODE_ENV || 'development',
    HOST: process.env.HOST || '0.0.0.0',
    PORT: process.env.PORT || 3000,
    FIUBA_URL:  process.env.BASE_FIUBA_URL ||'http://www.test.com/'
}