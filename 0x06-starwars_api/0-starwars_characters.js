#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs[0]) {
  const request = require('request');
  const url = `https://swapi-api.hbtn.io/api/films/${myArgs[0]}/`;
  request(url, (err, resp, body) => {
    if (err || resp.statusCode !== 200) console.log(err);
    else {
      const chList = JSON.parse(body).characters;
      const res = new Array(chList.length);
      let i = 0;
      for (let x = 0; x < chList.length; x++) {
        request(chList[x], (xerr, xresp, xbody) => {
          if (xerr || xresp.statusCode !== 200) console.log(xerr);
          else {
            res[x] = JSON.parse(xbody).name;
            i++;
          }
          if (i === chList.length) {
            for (let i = 0; i < chList.length; i++) {
              console.log(res[i]);
            }
          }
        });
      }
    }
  });
}