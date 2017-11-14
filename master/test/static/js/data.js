/**
 * Created by zero on 2017/8/26.
 */

import axios from 'axios'

class GETDATA {

  weekgaplist() {
    return axios.get('/8')
  }

  getonegap() {
    return axios.get('/9')
  }

}


export default GETDATA