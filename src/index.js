const app = require("./server");
const config = require('./Configuration/config');

async function init() {
    app.listen(config.PORT, config.HOST);
    console.log(`Running on http://${config.HOST}:${config.PORT}`);
}

init();
