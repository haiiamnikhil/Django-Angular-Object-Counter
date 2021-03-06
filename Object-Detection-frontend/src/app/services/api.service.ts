import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  header = new HttpHeaders({'Content-Type': 'application/json'})

  private messageSource = new BehaviorSubject<any>(0);
  currentmessage = this.messageSource.asObservable();
  
  constructor(private http:HttpClient) { }

  
  setMessages(message:any){
    const files = sessionStorage.setItem('files', JSON.stringify(message))
    this.messageSource.next(message)
  }

  sendImage(image:any):Observable<any>{
    return this.http.post('/process-image/',image)
  }
  downloadImage(image:any):Observable<any>{
    return this.http.post('/download-image/',image)
  }

  getMultiDetection(files:any):Observable<any>{
    return this.http.post('/multi-image-processor/',files)
  }

  login(credentials:any):Observable<any>{
    return this.http.post('/login-auth/',credentials,{headers:this.header})
  }

  register(credentials:any):Observable<any>{
    return this.http.post('/register-auth/',credentials,{headers:this.header})
  }

  isLoggedIn():Observable<any>{
    return this.http.post('/is-authenticated/',{headers:this.header})
  }

  logoutUser():Observable<any>{
    return this.http.get('/logout',{headers:this.header})
  }

  userDetails():Observable<any>{
    return this.http.get('/user-details/',{headers:this.header})
  }

}