<template>
  <div class="home">
    <div class="digui">
      <ul>
        <items v-for="(model,index) in list" :model="model" :key="index"><v-icon size="36" color="#efefef" style="float: left;" class="df-icon">lock</v-icon></items>
      </ul>
    </div>
  </div>
</template>
 
<script>
  import items from './items'
  export default {
    name: "Home",
    data() {
      return {
        list: [
          {
            "menuName": "项目管理",
            "level":1,
            "childTree": [{
              "menuName": "项目进度",
              "level":2,
              "childTree": [{
                "menuName": "项目一",
                "level":3,
                "childTree": [{ "menuName": "详细信息","level":4,"childTree":[] }]
              }]
            }, {
              "menuName": "任务安排",
              "level":2,
              "childTree":[]
            }]
          },
          {
            "menuName": "数据统计",
            "level":1,
            "childTree":[{
                "menuName": "店铺积分统计",
                "level":2,
                "childTree": [{
                    "menuName": "店铺积分统计",
                    "level":2,
                    "childTree": []
                }]
            }]
          },
          {
            "menuName": "人员管理",
            "level":1,
            "childTree":[]
          }]
      }
    },
    components:{
      items
    }
  }
</script>
 
<style scoped>


</style>