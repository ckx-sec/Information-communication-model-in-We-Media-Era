<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style>
  /*
   * 解决ElementUI表格线不对齐
   */
  body .el-table th.gutter {
    display: table-cell !important;
  }
</style>
