<template>
  <div class="home">
    <p class="heading">Select text to view more info</p>
    <div class="box">
      <ul>
        <li v-for="(t, index) in x" :key="index" @click="router()">
          <div  @click="router(t.text)" class="li-element">
            <div class="img-container">
              <img src="../images/text-format.png" alt="" />
            </div>
            <p class="meet-text">
    
              {{t.text}}
            </p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      message: "a",
      topic: [],
      final:[],
      x:[],
      id: 0,
     
    };
  },
  async mounted() {
    //  let params = {
    //   id: this.id
    // };
      
    // let res = await axios.get("http://127.0.0.1:5000/api/getRealTimeItems", {
    //   params
    // });
    //    if(res.data.msg!="end")
    // {
    //     this.topic = [];
    //     this.topic.push(res.data)
    // }
  
    
    // this.arrayslice()
   
    this.interval = setInterval(async() => {

      ++this.id;

       let params = {
      id: this.id
    };
      console.log(params)
    let res = await axios.get("http://127.0.0.1:5000/api/getRealTimeItems", {
      params
    });
    // this.topic = []
    if(res.data.msg!="end")
    {
        this.topic = [];
        this.topic.push(res.data)
    }
  
    
    this.arrayslice()
    }, 4000);


  },
  methods: {
    router(x) {
      this.$router.push({ name: "Dashboard", params: { id: 1 , st:x} });
    },
    arrayslice()
    {
      console.log(this.topic)
      this.final = [];
      this.final.push(this.topic[0].data)
      this.x=this.final[0]
      console.log(this.x)
      for(let i=0;i<this.topic.length;i++)
      {
        if(this.topic[i].msg=="end")
        {
          console.log("end here")
          clearInterval(this.interval);
          console.log("cleared")
        }
      }
      // console.log("this is topic")
      // console.log(this.topic)
      // console.log("this is element")
      // console.log(this.topic[0])
    }
  }
};
</script>

<style lang="scss" scoped>
.box {
  overflow-y: scroll;
  position: fixed;
  width: 75vw;
  height: 78vh;
  left: 50%;
  top: 58%;
  transform: translate(-50%, -50%);
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  padding: 10px;

  ul {
    list-style: none;
    width: 100%;

    margin: 0;
    padding: 0;
    margin: 0 auto;
  }

  li {
    padding-bottom: 10px;
  }

  .li-element:hover {
    background-color: #ebebeb;
  }
}

.li-element {
  cursor: pointer;
  // border: solid red;
  width: 100%;
  min-height: 30px;
  display: flex;
  align-items: center;
}
.heading {
  position: absolute;
  left: 50%;
  top: 12%;
  transform: translate(-50%, -50%);
  width: fit-content;
  font-size: 24px;
  font-weight: 600;
}

p {
  margin: 0;
  padding: 0;
}

.img-container {
  width: 40px;
  height: initial;
  //border: solid blue;
  display: flex;
  align-items: center;

  img {
    width: 45px;
    height: 45px;
  }
}

.meet-text {
  margin-left: 10px;
}
</style>
