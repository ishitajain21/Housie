function GenTable(list){
    var mainTable = document.getElementById("maintable");
    document.getElementById("ABC") += list;
    for (i=0;i <=8;i++){
      var tr = document.createElement("tr");
      mainTable.appendChild(tr);
      nextRow(i);
  
    }
    
  }
  
  function nextRow(i){
    var mainTable = document.getElementById("maintable");
     var tr = document.createElement("tr");
    
    for (k=1;k <=10;k++){
      var td1 = document.createElement("td");
      var text1 =  document.createTextNode(i*10+k);
      var step2 = i*10+k;
      var text2 = "a"+ step2.toString();
  
      td1.appendChild(text1);
      // console.log(text2);
      td1.id = text2;
      tr.appendChild(td1);
      mainTable.appendChild(tr);
  
    }
  }
  

    //   function highlight(list){
        
    //     for(i=0;i<list.length;i++){
    //       ele = list[i];
    //       ide = "a" + ele.toString();
    //       document.getElementById("ABC") += "HELLOOO!!" + ide;
    //   }
    // }