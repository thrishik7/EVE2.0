
const express = require('express')
const fs= require('fs')
const https= require('https')
const path = require('path')


const app= express()
const directoryToServe = 'client'
const port = 3443

app.use('/', express.static)