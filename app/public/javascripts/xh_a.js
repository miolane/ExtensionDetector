var URL = "/app";

window.onload = sideway;

function sideway() {
    $.get(URL, function (html) {
        var origin = parseDom(html);
        var changes = compare(origin, document);
        pushData('/pushapp', changes);
    })
}

function main() {
    getRawHTML(URL, function (origin) {
        var changes = compare(origin, document);
        console.log(changes);
        pushData('/pushapp', changes);
    });
}


function getRawHTML(url, callback)
{
    var ajax = new XMLHttpRequest();
    var rawText;
    ajax.onreadystatechange = function () {
        if (ajax.readyState === 4 && ajax.status === 200)
        {
            rawText = ajax.responseText;
            let origin = parseDom(rawText);
            callback(origin);
        }
    };

    ajax.open('get', url, true);
    ajax.send(null);

}


function parseDom(html)
{
    const d = document.cloneNode(true);
    d.innerText = "";
    d.write(html);
    return d;
}


function parseChange(node, changeType)
{
    var p;
    if(node.parentElement !== window)
    {
        p = node.parentElement;
    } else
    {
        p = null;
    }
    return {
        "parent": p ? p.tagName: "",
        "node": node.outerHTML.substr(0, 100),
        "change": changeType
    };
}


function compare(origin, changed)
{
    function eq(a, b)
    {
        return (a.tagName.toString() === b.tagName.toString()) && (a.className.toString() === b.className.toString()) && (a.id.toString() === b.id.toString());
    }

    var changes = [];
    // 同步模拟
    var current = origin, current_shadow = changed;
    var stack = [], stack_shadow = [];
    stack.push(origin);
    stack_shadow.push(changed);
    while(stack.length){
        current = stack.shift();
        current_shadow = stack_shadow.shift();
        var i_shadow = 0;
        for(var i = 0; i < current.children.length; i ++)
        {
            var nodei = current.children[i];
            var found = false;
            for(var j = i_shadow; j < current_shadow.children.length; j ++)
            {
                var nodej = current_shadow.children[j];
                if(eq(nodei, nodej))
                {
                    found = true;
                    for(var t = i_shadow+1; t < j; t ++)
                    {
                        changes.push(parseChange(current_shadow.children[t], "addNode"));
                    }
                    i_shadow = j;
                    if(nodei.hasChildNodes() && nodej.hasChildNodes())
                    {
                        stack.push(nodei);
                        stack_shadow.push(nodej);
                    } else
                    {
                        if(nodei.outerHTML !== nodej.outerHTML)
                        {
                            changes.push(parseChange(nodei, "modifyContent"));
                        }
                    }
                    break;
                }
            }
            if(!found)
            {
                changes.push(nodei, parseChange(nodei, "delNode"));
            }
        }
        for(t = i_shadow+1; t < current_shadow.children.length; t ++)
        {
            changes.push(parseChange(current_shadow.children[t], "addNode"));
        }
    }
    return changes;
}

function pushData(url, diffs)
{
    $.post(url, {"data": JSON.stringify({"diffs": diffs})}).done(function (res) {
        console.log(res);
        var p = document.createElement("p");
        p.innerText = res;
        document.body.append(p);
    })
}