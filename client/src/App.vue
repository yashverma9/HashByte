<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->

    <div class="nav">
      <h1 id="hashcash">hashbyte</h1>
       <span id="menu" style="font-size:30px;cursor:pointer;color:white;" @click="openNav()"
        >&#9776; </span>
      
     
      
      <div id="mySidenav" class="sidenav">
        <a href="javascript:void(0)" class="closebtn" @click="closeNav()"
          >&times;</a
        >
        <a href="/">Home</a>
        <a href="/save">Saved Items</a>
        <a href="/dashboard">Dashboard</a>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    openNav() {
   
      document.getElementById("mySidenav").style.width = "250px";
    },
    closeNav() {
     document.getElementById("mySidenav").style.width = "0";
     
    }
  }
};
</script>



<style lang="scss" scoped></style>

<style lang="scss">
html,
body {
  margin: 0;
  padding: 0;
  background-color: #e5e5e5;
  font-family: "Poppins", sans-serif;
}

.nav {
  width: 100vw;
  height: 50px;
  background-color: #195ed8;
  
}

#hashcash {
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

.sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #FFFFFF;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
}

.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;
}

.sidenav a:hover {
  color: #195ed8;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav a {
    font-size: 18px;
  }
}

#menu{
  position: absolute;
  top: 0%;
  left: 1%;
}
</style>
