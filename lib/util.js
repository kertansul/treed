
function extend(a, b) {
  for (var c in b) {
    a[c] = b[c]
  }
  return a
}

function make_listed(data, nextid, collapse) {
  var ids = {}
    , children = []
    , ndata = {}
    , res
  if (undefined === nextid) nextid = 100

  if (data.nodes) {
    for (var i=0; i<data.nodes.length; i++) {
      res = make_listed(data.nodes[i], nextid, collapse)
      for (var id in res.tree) {
        ids[id] = res.tree[id]
      }
      children.push(res.id)
      nextid = res.id + 1
    }
    // delete data.nodes
  }
  for (var name in data) {
    if (name === 'nodes') 
      continue
    else if(name === 'text')
      ndata['name'] = data['text']
    else
      //ndata[name] = data[name]
      continue
  }
  ndata.done = false
  ids[nextid] = {
    id: nextid,
    data: ndata,
    children: children,
    collapsed: !!collapse
  }
  for (var i=0; i<children.length; i++) {
    ids[children[i]].parent = nextid;
  }
  return {id: nextid, tree: ids}
}



