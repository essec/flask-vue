<template>
<div>
  
  
  <div class="row center">
      <button class="ui button" id="sidebar">menu</button>
  </div>
<div class="ui left demo vertical inverted sidebar labeled icon menu">
  <a class="item">
    <i class="home icon"></i>
    Home
  </a>
  <a class="item">
    <i class="block layout icon"></i>
    Topics
  </a>
  <a class="item">
    <i class="smile icon"></i>
    Friends
  </a>
  
</div>
</div>
</template>

<script>
//init semantic function
$(function(){
    $("#test").click(function(){
        $('.modal').modal('show');
    });
    $(".modal").modal({
        closable: true
      });
    $("#sidebar").click(function(){
      $('.ui.labeled.icon.sidebar').sidebar('toggle')
    })
    
;
})


</script>

