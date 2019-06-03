# abelit-DataScience

## frontend
Vue在密码框使用“ @keyup.enter="submit" ”绑定“Enter回车键”可以实现敲击回车键进行响应
```javascript
  @keyup.enter="submit"
```

Vue通过@focus和@blur来监听焦点事件
```
 @focus="checkUser"
 @blur="checkUser"
```

Vue Prop属性
props用与接收父组件传递给子组件的值

VuePropDemo为父组件
```javascript
//VuePropDemo.vue
<template>
    <div>
        <h1>VuePropDemo 父组件</h1>
        <vue-prop-demo-a pname="yanghui"></vue-prop-demo-a>
    </div>
</template>


<script>
import VuePropDemoA from "@/components/demo/VuePropDemoA";

export default {
    components: {
        VuePropDemoA
    }
}
</script>
```

VuePropDemoA为子组件
```javascript
//VuePropDemoA.vue
<template>
    <div>
        <h1>VuePropDemoA 子组件A</h1>
        <p>{{ pname }}</p>
    </div>
</template>

<script>
export default {
    data () {
        return {}
    },
    props: ["pname"]
}
</script>
```

### 使用vue-perfect-scrollbar遇到的问题
```
<vue-perfect-scrollbar
      :class="isPageFullScreen?'d-page-scroll-fullscreen ps':'d-page-scroll ps'"
      @ps-scroll-y="scrollHanle"
    >
......
</vue-perfect-scrollbar>
```
***注意：在使用vue-perfect-scrollbar组件来做页面的滚动条时，需要在class属性中带上"ps"属性来避免该组件在全屏或退出全屏时造成的页面高度继承所产生的页面高度错误！***

## Git&Github使用手册
### 0. Git配置
```
git config --global user.name "abelit"
git config --global user.email "ychenid@live.com"
```
### 1.Git分支
```bash
# 创建分支company
git branch company

# 切换到company分支
git checkout company

# 在company分支中合并master分支的内容
git merge master
```

### 2.Git Tag
```bash
# -a后面指定版本号，-m后面跟说明信息
git tag -a v0.1.alpha  -m "base frontend and backend structure"

# 提交tag版本到远程git仓库
git push origin --tags

# 删除本地仓库tag
git tag -d v0.1.alpha

# 删除远程仓库tag
git push origin :refs/tags/v0.1.alpha
```
