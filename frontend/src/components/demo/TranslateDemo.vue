<template>
  <div class="headerComponent">
      <a href="#/trans" class="h-logo" @click="changeLangEvent()">
        {{$t('m.translate')}}
      </a>
      <li> {{$t('m.music')}}</li>
      <li>{{ $t('m.friend') }}</li>
      <li>{{ $t('m.download') }}</li>
      <li>{{ $t('m.musician') }}</li>

      <form id="app" @submit="checkForm" action="/something" method="post" novalidate="true">
  
  <p v-if="errors.length">
    <b>Please correct the following error(s):</b>
    <ul>
      <li v-for="error in errors">{{ error }}</li>
    </ul>
  </p>
  
  <div class="form-group">
    <p>
    <label for="name">Name</label>
    <input type="text" name="name" id="name" class="form-control" v-model="name">
  </p>
  </div>

<div class="form-group">
    <p>
    <label for="email">Email</label>
    <input type="email" name="email" id="email" class="form-control" v-model="email">
  </p>
</div>



<div class="form-group">
   <p>
    <label for="movie">Favorite Movie</label>
    <select name="movie" id="movie" class="form-control" v-model="movie">
      <option>Star Wars</option>
      <option>Vanilla Sky</option>
      <option>Atomic Blonde</option>
    </select>
  </p>

  <p>
    <input type="submit" value="Submit">  
  </p>

<!-- <input type="text" placeholder="邮箱" v-validate ="'required|email'" name="email"/>
<span class="errortip" v-show="errors.has('email')">{{ errors.first('email')}}</span>
<button type="button" class="btn btn-primary">commit</button> -->
  
</div>

</form>
  </div>
</template>
<script>
    export default {
        data () {
          return {
            lang: 'zh_CN',
            errors:[],
            name:null,
            email:null,
            movie:null
          }
        },
        methods: {
            /**
             * 切换语言 
             */ 
            changeLangEvent() {
              this.$confirm(this.$t('m.hintContent'),this.$t('m.hint'), {
                confirmButtonText: this.$t('m.confirm'),
                cancelButtonText: this.$t('m.cancel'),
                type: 'warning'
              }).then(() => {
                if ( this.lang === 'zh_CN' ) {
                  this.lang = 'en_US';
                  this.$i18n.locale = this.lang;
                }else {
                  this.lang = 'zh_CN';
                  this.$i18n.locale = this.lang;
                }
              }).catch(() => {
                this.$message({
                  type: 'info',
                });          
              });
            },
            checkForm:function(e) {
      this.errors = [];
      if(!this.name) this.errors.push(this.$t('m.nameRequired'));
      if(!this.email) {
        this.errors.push(this.$t('m.emailRequired'));
      } else if(!this.validEmail(this.email)) {
        this.errors.push("Valid email required.");        
      }
      if(!this.errors.length) return true;
      e.preventDefault();
    },
    validEmail:function(email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
    }
        },
        mounted: function() {
        }
    }
</script>
<style scoped>
.headerComponent{
    padding-top: 80px;
    width: 100%;
    height: 70px;
    background-color: #242424;
}
input,select {
  margin-left: 10px;
}
</style>