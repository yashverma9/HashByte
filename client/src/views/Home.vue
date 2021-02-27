<template>
  <div class="home">
    <p class="heading">Select text to view more info</p>
    <div class="box">
      <ul>
        <li>
          <div class="li-element">
            <div class="img-container">
              <img src="../images/text-format.png" alt="" />
            </div>
            <p class="meet-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris ni
            </p>
          </div>
        </li>

        <li>
          <div class="li-element">
            <div class="img-container">
              <img src="../images/text-format.png" alt="" />
            </div>
            <p class="meet-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris ni
            </p>
          </div>
        </li>

             <li>
          <div class="li-element">
            <div class="img-container">
              <img src="../images/text-format.png" alt="" />
            </div>
            <p class="meet-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris ni

                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris ni


                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris ni
            </p>
          </div>
        </li>

             <li>
          <div class="li-element">
            <div class="img-container">
              <img src="../images/text-format.png" alt="" />
            </div>
            <p class="meet-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labboris ni
            </p>
          </div>
        </li>

             <li>
          <div class="li-element">
            <div class="img-container">
              <img src="../images/text-format.png" alt="" />
            </div>
            <p class="meet-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris ni

                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris ni
            </p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  data() {
    return {
      key: 1
    };
  },
  methods: {
    name() {}
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
