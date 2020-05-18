import React from 'react'
import { Switch, Route } from 'react-router-dom'

import Home from '../pages/home'
import RegisterUser from '../pages/register-user'
import Login from '../pages/login'
import Monitor from '../pages/monitor'

function Routes() {
  return (
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/register-user" exact component={RegisterUser} />
      <Route path="/login" exact component={Login} />
      <Route path="/monitor" exact component={Monitor} />
    </Switch>
  )
}

export default Routes