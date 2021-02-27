<template>
  <div>
    <div class="definition box">
      <div class="save">
        <p>Saved Items</p>
      </div>

      <div class="def-box white-box">
        <table>
          <tr>
            <th>No</th>
            <th>Text</th>
            <th>Source</th>
            <th>Link</th>
          </tr>
          <tr v-for="(f, index) in final" :key="index">
            <td>{{index +1}}</td>
            <td>
              {{f.definition}}
            </td>
            <td>Audio</td>
            <td>
              <div  @click="open(f.id)" class="save-button">
                <p>Open</p>
              </div>
            </td>
          </tr>
         
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Save",
  async mounted() {
    let res = await axios.get("http://127.0.0.1:5000/api/getAllItem");
    this.data=res.data;
    console.log(this.data);
    for(let i=0; i<this.data.length;i++)
    {
        if(this.data[i].selected == 1)
        {
            this.final.push(this.data[i])
            console.log(this.final)
        }
    }
  },
  data() {
    return {
      data: [],
      final: []
    };
  },
  methods: {
    open(x) {
        console.log(x)
        this.$router.push({ name: 'Savedashboard', params: { id: x } })
    }
  }
};
</script>

<style lang="scss" scoped>
.definition {
  //   position: relative;
  //   min-height: 55vh;
  //   max-height: max-content;
  padding-bottom: 35px;
  margin-top: 60px !important;

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

.def-box {
  margin-top: 10px;
  min-height: 30vh;
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
      font-size: 14px;
      line-height: 21px;

      color: #000000;
    }
    span {
      margin-top: 10px;
      margin-right: 15px;
    }
  }
}

.box {
  width: 80vw;
  margin: 0 auto;
  background-color: #195ed8;
  border-radius: 5px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}
// th{
//     text-align: center;
// }

tr:hover {
  background-color: #f5f5f5;
}

.save-button {
  //margin-left: 270px;

  margin: 0 !important;
  cursor: pointer;
  width: 97px;
  height: 34px;
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
</style>
