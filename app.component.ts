import { ApplicationRef, Component } from '@angular/core';
import { HeroesComponent } from "./heroes/heroes.component";
import { HeroDetailComponent} from "./hero-detail/hero-detail.component";
import { MessagesComponent } from "./messages/messages.component";
import { RouterModule, Routes } from '@angular/router';



@Component({
  selector: 'app-root',
  standalone:true,
  imports: [MessagesComponent,RouterModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',

})
export class AppComponent {
  title = 'Tour Of Heroes';
  constructor() {
 
  }

}
