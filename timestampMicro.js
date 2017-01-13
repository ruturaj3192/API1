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
	    var timestamp = process.argv[2];
	    //var date = new Date(timestamp*1000);
	    var monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
	    var naturalDate = new Date(timestamp);
	    var unixdate = new Date();
	    if(!isNaN(naturalDate.getDate()))
	    {
	        unixdate =  Date.parse(process.argv[2])/1000;
	        naturalDate = process.argv[2];
	    }
	    else if(isNaN(naturalDate.getDate()))
	    {
	        unixdate = new Date(timestamp*1000);
	        if(!isNaN(unixdate.getDate()))
	        {
                naturalDate = monthNames[unixdate.getMonth()]+' '+unixdate.getDate()+', '+unixdate.getFullYear();	 
                unixdate = process.argv[2];
	        }
	    }
	    reply(JSON.stringify({unix:unixdate, natural:naturalDate}));
	}
});

server.start((err) => {
	if(err){
		throw err;
	}
	console.log(`Server running at: ${server.info.uri}`);
});
