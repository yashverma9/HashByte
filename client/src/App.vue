<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    
    <div class="nav">
      <h1 id="hashcash" >hashcash</h1>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss" >
  html,body{

    margin: 0;
    padding: 0;
    background-color: #E5E5E5;
   font-family: 'Poppins', sans-serif;

  }

  .nav{
    width: 100vw;
    height: 50px;
    background-color: #195ED8;
  }

  #hashcash{
    margin: 0;
    padding: 0;
    color: #f0f0f0;
    text-align: center;
  }

  /* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}

</style>
