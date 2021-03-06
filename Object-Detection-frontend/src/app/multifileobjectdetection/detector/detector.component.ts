import { ApiService } from './../../services/api.service';
import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-detector',
  templateUrl: './detector.component.html',
  styleUrls: ['./detector.component.css']
})
export class DetectorComponent implements OnInit {
  get:any
  count:any
  report:any
  detectedImages:any
  constructor(private ApiService: ApiService, private router:Router) { }

  ngOnInit(){
    const file = JSON.parse(sessionStorage.getItem('files'));
    this.ApiService.currentmessage.subscribe(message =>{
      if(message){
        this.get = message.data
        this.report = message.csv[0]
        console.log(this.report)
      }
      else if(file){
        this.get = file.data
        this.report = file.csv[0]
        console.log(this.report)
      }
      else{
        this.router.navigate(['/multidetector'])
      }
    })
  }
  showImage(i:any){
    this.detectedImages = this.get[i]
  }
}
