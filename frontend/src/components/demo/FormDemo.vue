<template>
  <div class="hello">
    <div>
      <a href="#/form" class="h-logo" @click="changeLangEvent()">
        {{$t('m.translate')}}
      </a>
      <li> {{$t('m.music')}}</li>
      <li>{{ $t('m.friend') }}</li>
      <li>{{ $t('m.download') }}</li>
      <li>{{ $t('m.musician') }}</li>
    </div>
    <div class="input-group">
      <input class="form-control" :class="{ 'is-invalid': errors.has('email') }" type="email" v-validate="'required|email'" name="email" :placeholder="$t('m.email')">
      <div class="invalid-feedback">
          {{ errors.first('email') }}
      </div>
    </div>
      <form>
    <v-text-field
      v-model="name"
      v-validate="'required|max:10'"
      :counter="10"
      :error-messages="errors.collect('name')"
      label="Name"
      data-vv-name="name"
      required
    ></v-text-field>
    <v-text-field
      v-model="email"
      v-validate="'required|email'"
      :error-messages="errors.collect('email')"
      label="E-mail"
      data-vv-name="email"
      required
    ></v-text-field>
    <v-select
      v-model="select"
      v-validate="'required'"
      :items="items"
      :error-messages="errors.collect('select')"
      label="Select"
      data-vv-name="select"
      required
    ></v-select>
    <v-checkbox
      v-model="checkbox"
      v-validate="'required'"
      :error-messages="errors.collect('checkbox')"
      value="1"
      label="Option"
      data-vv-name="checkbox"
      type="checkbox"
      required
    ></v-checkbox>

    <v-btn @click="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>
  </div>
</template>

<script>
  export default {

    data: () => ({
      lang: 'zh_CN',
      name: '',
      email: '',
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4'
      ],
      checkbox: null,
      dictionary: {
        attributes: {
          email: 'E-mail Address 1'
          // custom attributes
        },
        custom: {
          name: {
            required: () => 'Name can not be empty',
            max: 'The name field may not be greater than 10 characters'
            // custom messages
          },
          select: {
            required: 'Select field is required'
          }
        }
      }
    }),

    mounted () {
    },

    methods: {
      submit () {
        this.$validator.validateAll()
      },
      clear () {
        this.name = ''
        this.email = ''
        this.select = null
        this.checkbox = null
        this.$validator.reset()
      },
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
                  this.$validator.locale = this.lang;
                }else {
                  this.lang = 'zh_CN';
                  this.$i18n.locale = this.lang;
                  this.$validator.locale = this.lang;
                }
              }).catch(() => {
                this.$message({
                  type: 'info',
                });          
              });
            }
    }
  }
</script>