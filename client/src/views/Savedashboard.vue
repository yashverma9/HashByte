<template>
  <div>
    <div v-bind:class="{ show: showpopup }" class="popup">
      <p id="ok-p">Save Successfull</p>
      <div id="ok" @click="popup()" class="save-button">
        <p>Ok</p>
      </div>
    </div>
    <div class="header">
      <div class="img-container">
        <img src="../images/text-format.png" alt="" />
      </div>
      <p style="font-size:28px;">
        Heart
      </p>
    </div>

    <div class="definition box">
      <div class="save">
        <p>Your Note</p>
        <!-- <div @click="save()" class="save-button">
          <p>save</p>
        </div> -->
      </div>

      <div style="padding:10px;" class="def-box white-box">
        <ul>
          <li>
            <p>
              {{ notee }}
            </p>
          </li>
        </ul>
      </div>
    </div>

    <div class="definition box">
      <div class="save">
        <p>Definition</p>
        <!-- <div @click="save()" class="save-button">
          <p>save</p>
        </div> -->
      </div>

      <div class="def-box white-box">
        <ul>
          <li>
            <span>#</span>
            <p>
              {{ definition }}
            </p>
          </li>
        </ul>
      </div>
    </div>

    <div class="related box">
      <div class="save">
        <p>Related Links</p>
        <!-- <div @click="save()" class="save-button">
          <p>save</p>
        </div> -->
      </div>
      <div class="related-box white-box">
        <ul>
          <li v-for="(l, index) in relatedLinks" :key="index">
            <span><img class="link-img" src="../images/link.png" alt=""/></span>
            <p>
              <a
                style="color:black; text-decoration:none;"
                target="blank"
                href=" https://en.wikipedia.org/wiki/Machine_learning"
              >
                {{ l }}
              </a>
            </p>
          </li>
        </ul>
      </div>
    </div>

    <div class="photos box">
      <div class="save">
        <p>Photos</p>
        <!-- <div @click="save()" class="save-button">
          <p>save</p>
        </div> -->
      </div>
      <div class="photos-box white-box">
        <ul>
          <li v-for="(i, index) in image" :key="index">
            <img :src="i" alt="" />
          </li>
        </ul>
      </div>
    </div>

    <div class="videos box">
      <div class="save">
        <p>Videos</p>
        <!-- <div @click="save()" class="save-button">
          <p>save</p>
        </div> -->
      </div>
      <div class="videos-box white-box">
        <ul>
          <li v-for="(v, index) in video" :key="index">
            <iframe
              class="vid"
              width="100%"
              height="100%"
              :src="v"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            ></iframe>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Savedashboard",

  data() {
    return {
      id: " ",
      data: [],
      definition: "",
      relatedLinks: [],
      image: [],
      video: [],
      note: "",
      showpopup: false,
      notee: ""
    };
  },
  created() {
    this.id = this.$route.params.id;
    console.log(this.$route.params);
  },
  watch: {
    // call again the method if the route changes
    $route: "/dashboard"
  },
  async mounted() {
    console.log("i am called");
    let params = {
      id: this.id
    };

    let res = await axios.get("http://127.0.0.1:5000/api/getCurrentItem", {
      params
    });

    console.log(res.data);
    this.definition = res.data.definition;
    this.relatedLinks = res.data.relatedLinks;
    this.image = res.data.image;
    this.video = res.data.video;
    this.notee = res.data.note;
  },
  methods: {
    notes(x) {
      this.note = x;
      console.log(this.note);
    },
    async save() {
      console.log("posted");
      let params = {
        id: this.id
      };
      let a = await axios.get("http://127.0.0.1:5000/api/saveItem", { params });
      console.log(a);

      this.api2();
      this.popup();
    },
    popup() {
      this.showpopup = !this.showpopup;
    },
    async api2() {
      let params = {
        id: this.id,
        note: "fwsfg"
      };
      console.log(params);

      let b = await axios.get("http://127.0.0.1:5000/api/postNote", { params });
      console.log(b);
    }
  }
};
</script>

<style lang="scss" scoped>
.header {
  width: 80vw;
  height: 15vh;
  margin: 0 auto;
  background-color: #195ed8;
  border-radius: 5px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  margin-top: 30px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  p {
    font-family: "Poppins", sans-serif;
    font-size: 18px;
    color: #ffffff;
    width: 80%;
  }
  //   padding: 10px;
}
.box {
  width: 80vw;
  margin: 0 auto;
  background-color: #195ed8;
  border-radius: 5px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.white-box {
  width: 70vw;
  margin: 0 auto;
  //   position: absolute;
  //   top: 50%;
  //   left: 50%;
  //   transform: translate(-50%, -50%);
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
}

.img-container {
  width: 74px;
  height: 73.63px;
  background: #023794;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  img {
    width: 80%;
    height: 80%;
  }
}

.definition {
  //   position: relative;
  //   min-height: 55vh;
  //   max-height: max-content;
  padding-bottom: 35px;
  margin-top: 20px;

  p {
    margin: 0;
    padding: 0;
    padding-left: 20px;
    padding-top: 10px;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
    font-size: 36px;
    color: #ffffff;
    width: fit-content;

    // position: absolute;
    // top: 10%;
    // left: 16%;
    // transform: translate(-50%, -50%);
  }
}

.related {
  //   position: relative;
  //   height: 45vh;
  margin-top: 20px;
  padding-bottom: 35px;

  p {
    margin: 0;
    padding: 0;
    padding-left: 20px;
    padding-top: 10px;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
    font-size: 36px;
    color: #ffffff;
    width: fit-content;

    // position: absolute;
    // top: 10%;
    // left: 16%;
    // transform: translate(-50%, -50%);
  }
}

.photos {
  padding-bottom: 35px;
  position: relative;
  height: fit-content;
  max-height: 88vh;

  margin-top: 20px;

  p {
    margin: 0;
    padding: 0;
    padding-left: 20px;
    padding-top: 10px;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
    font-size: 36px;
    color: #ffffff;
    width: fit-content;

    // position: absolute;
    // top: 10%;
    // left: 16%;
    // transform: translate(-50%, -50%);
  }
}

.videos {
  position: relative;
  height: 65vh;
  margin-top: 20px;

  p {
    margin: 0;
    padding: 0;
    padding-left: 20px;
    padding-top: 10px;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
    font-size: 36px;
    color: #ffffff;
    width: fit-content;

    // position: absolute;
    // top: 10%;
    // left: 16%;
    // transform: translate(-50%, -50%);
  }
}

.def-box {
  min-height: 13vh;
  max-height: max-content;
  ul {
    list-style: none;
    // border: dotted red;
    width: 80%;
    margin: 0 auto;
    margin-top: 20px;
    padding: 0;
  }
  li {
    display: flex;

    padding-bottom: 10px;
    p {
      font-family: Poppins;
      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 21px;

      color: #000000;
    }
    span {
      margin-top: 10px;
      margin-right: 15px;
    }
  }
}

.related-box {
  min-height: 20vh;
  max-height: max-content;
  ul {
    list-style: none;
    // border: dotted red;
    width: 80%;
    margin: 0 auto;
    margin-top: 20px;
    padding: 0;
    padding-top: 18px;
  }
  li {
    display: flex;

    padding-bottom: 10px;
    p {
      // width: 10px;
      font-family: Poppins;
      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 21px;

      color: #000000;
    }
    span {
      margin-top: 12px;

      margin-right: 15px;
    }
  }
}

.photos-box {
  //   padding: 10px;
  max-height: 70vh;
  overflow-y: scroll;
  ul {
    padding: 0;
    //border: dotted red;
    list-style-type: none;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    li {
      //   padding: 2rem;
      //   margin:1rem;
    }
  }
  img {
    max-width: 400px;
    max-height: 400px;
  }
}

.videos-box {
  overflow-y: scroll;
  height: 45vh;
  ul {
    margin: 0;
    padding: 0;
    // border: dotted red;
    list-style-type: none;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    li {
      // border: dotted green;
      width: 100%;
      height: 300px;
      //   padding: 2rem;
      margin: 1rem;
    }
  }
}

.link-img {
  width: 18px;
  height: 18px;
}

.vid {
  margin: 0 auto;
}

.save {
  //border: dotted red;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  position: relative;
}

.save-button {
  //margin-left: 270px;
  position: absolute;
  right: 6%;
  cursor: pointer;
  width: 111px;
  height: 31px;
  background: #faee1c;
  border-radius: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
  p {
    margin: 0;
    padding: 0;
    font-family: Poppins;
    font-style: normal;
    font-weight: 500;
    font-size: 18px;
    line-height: 27px;

    color: #090909;
  }
}

.save-button:hover {
  background: rgb(211, 203, 43);
}

#text-area {
  border: none;
  width: 100%;
  height: 99%;
  outline: #195ed8;
}

.popup {
  display: none;
  width: 70vw;
  height: 18vh;
  background: #195ed8;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  border-radius: 5px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

#ok {
  position: fixed;
  top: 80%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
#ok-p {
  font-size: 30px;
  font-weight: 500;
  text-align: center;
  color: #ffffff;
}
.show {
  display: block;
}
</style>
