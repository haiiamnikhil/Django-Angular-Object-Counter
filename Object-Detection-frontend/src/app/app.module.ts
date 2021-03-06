import { ApiService } from './services/api.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ObjectcountComponent } from './objectcount/objectcount.component';
import { FormsModule } from '@angular/forms';
import { ObjectdetectorComponent } from './objectdetector/objectdetector.component';
import { MultifileobjectdetectionComponent } from './multifileobjectdetection/multifileobjectdetection.component';
import { CategorieselectorComponent } from './categorieselector/categorieselector.component';
import { DetectorComponent } from './multifileobjectdetection/detector/detector.component';
import { LoginComponent } from './user/login/login.component';
import { RegisterComponent } from './user/register/register.component';
import { ChangepasswordComponent } from './user/changepassword/changepassword.component';
import { ProfileComponent } from './user/profile/profile.component';
import { LogoutComponent } from './user/logout/logout.component';
import { environment } from '../environments/environment';
import { NavbarComponent } from './navbar/navbar.component';
import { DraganddropComponent } from './draganddrop/draganddrop.component';
import { DragndropDirective } from './directives/dragndrop.directive'

@NgModule({
  declarations: [
    AppComponent,
    ObjectcountComponent,
    ObjectdetectorComponent,
    MultifileobjectdetectionComponent,
    CategorieselectorComponent,
    DetectorComponent,
    LoginComponent,
    RegisterComponent,
    ChangepasswordComponent,
    ProfileComponent,
    LogoutComponent,
    NavbarComponent,
    DraganddropComponent,
    DragndropDirective
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
