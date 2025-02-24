import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Hero } from './heroes/hero';
import { HEROES } from './heroes/mock.heroes';


@Injectable({
  providedIn: 'root'
})
export class MessageService {  
   
  messages :string[]=[];
  messageService: any;

  
  
  add(message:string)
  {this.messages.push(message);}
  clear(){
    this.messages=[];
  }
  

}

