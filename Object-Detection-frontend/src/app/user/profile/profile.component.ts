import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  userdetails = []
  constructor(private apiService: ApiService) { }

  ngOnInit(){
    this.apiService.userDetails().subscribe(response => {
      if(response.status){
        this.userdetails.push(response.message);
      }
    },
    error=>console.log(error))
  }

}
