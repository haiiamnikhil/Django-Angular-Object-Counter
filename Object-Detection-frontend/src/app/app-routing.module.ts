import { MultifileobjectdetectionComponent } from './multifileobjectdetection/multifileobjectdetection.component';
import { ObjectdetectorComponent } from './objectdetector/objectdetector.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ObjectcountComponent } from './objectcount/objectcount.component';
import { CategorieselectorComponent } from './categorieselector/categorieselector.component';
import { DetectorComponent } from './multifileobjectdetection/detector/detector.component';
import { LoginComponent } from './user/login/login.component';
import { RegisterComponent } from './user/register/register.component';
import { LogoutComponent } from './user/logout/logout.component';
import { ProfileComponent } from './user/profile/profile.component';
import { DraganddropComponent } from './draganddrop/draganddrop.component';


const routes: Routes = [
  {
    path:'',
    component:CategorieselectorComponent
  },
  {
    path:'login',
    component:LoginComponent
  },
  {
    path:'register',
    component:RegisterComponent
  },
  {
    path:'logout',
    component:LogoutComponent
  },
  {
    path:'profile',
    component:ProfileComponent
  },
  {
    path:'draganddrop',
    component:DraganddropComponent
  },
  {
    path:'singledetector',
    component:ObjectdetectorComponent
  },
  {
    path:'multidetector',
    component: MultifileobjectdetectionComponent
  },
  {
    path:'multidetector/detector',
    component: DetectorComponent
  },
  {
    path: 'show-output',
    component: ObjectcountComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
