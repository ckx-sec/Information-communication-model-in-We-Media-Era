<template>
  <div class="dashboard-container">
    <!-- frameborder属性：不设置边框，如果是vue2.x版本，那么可以使用src属性 -->
    <iframe :src="tempHtml" ref="iframe" style="width: 100%; height: 800px;" frameborder="0" />
  </div>
</template>

<script>
import jsCookie from "js-cookie";

export default {
  name: "Dashboard",
  data() {
    // 我的外部文件是temp.html
    return {
      type: jsCookie.get("type"),
      name: jsCookie.get("username"),
      tempHtml: '../lines.html',
    };
  },
  computed: {
    // ...mapGetters([
    //   'name'
    // ])
  },
  mounted() {
    console.log("store:");
    console.log(jsCookie.get("userId"));
  },
};
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
