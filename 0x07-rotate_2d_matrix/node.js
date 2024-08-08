const express = require('express')
const app = express()

// this automatically allows you to 
// to route to all the static files, including 
// images without defining any route for them.
// public is the root directory
app.use(express.static('public') )

app.get('/', (reg, res) =>{
    res.send("This is the root")
})

app.listen(3005, ()=>{
    console.log("app listening on port 3005")
})
