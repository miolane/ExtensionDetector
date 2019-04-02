# ExtensionDetector

A project for *Network Security*


## Interface
#### Load extension:
domain/detect?ext=\<extension name\>
#### Template provides:
One pug file consists of all DOM nodes collected
#### Collect interesting node
Scan extension source code and pull them out. Save it as JSON.

Insert hooks. Insert some codes after the interesting function like "getElementXXX" or "$('.XXX'|'#XXX')"
``` js
var foo = document.getElementByXX(); // copy the function from above
var data = foo.parent.innerText;
var s = document.createElement("script").setAttribute("src", 'https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js');
document.head.appendChild(s);
$.post('localhost:3000/collect', {"data": data});
```
