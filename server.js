var express = require('express')
//var app = express()
'use strict';
const Hapi = require("hapi");


const server = new Hapi.Server();
server.connection({ port : 8080 });
server.route({
	method : 'GET',
	path : '/',
	handler : function(request,reply){
		reply('Hello Chandu!');
	}
});


server.start((err) => {
	if(err){
		throw err;
	}
	console.log(`Server running at: ${server.info.uri}`);
});
