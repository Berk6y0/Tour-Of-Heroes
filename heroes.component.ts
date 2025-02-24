import { Component, OnInit} from '@angular/core';
import { Hero } from './hero';
import { HEROES } from './mock.heroes';
import { CommonModule } from '@angular/common';
import { HeroDetailComponent } from "../hero-detail/hero-detail.component";
import { HeroService } from '../hero.service';
import { MessageService } from '../message.service';
import { RouterModule } from '@angular/router';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-heroes',
  standalone:true,
  imports: [CommonModule,RouterModule,],
  templateUrl: './heroes.component.html',
  styleUrl: './heroes.component.css'
})
export class HeroesComponent implements OnInit{
  heroes:Hero[]=[];
  selectedHero?:Hero;
  constructor(private heroService:HeroService, private messageService:MessageService, private cdr: ChangeDetectorRef){}
  ngOnInit():void{
    this.getHeroes();
  }
  onSelected(hero:Hero):void{
    this.selectedHero=hero;
    this.messageService.add(`You selected Hero with id of${hero.id} and name ${hero.name}`)
   
   console.log(hero);
  }
  
  getHeroes():void{
  this.heroService.getHeroes()
      .subscribe(x=>this.heroes=x)
  }
  add(name:string,imageUrl:string):void{
    name=name.trim();
    imageUrl=imageUrl.trim();
    if(!name){return;}
    if(!imageUrl){return;}
    this.heroService.addHero({name,imageUrl} as Hero).subscribe(hero=>{this.heroes.push(hero)});
    this.cdr.detectChanges();
    window.location.reload();
    this.messageService.add(`new hero added hero list`);
  }

  delete(hero:Hero):void{
    this.heroes=this.heroes.filter(h=> h!==hero);
    this.heroService.deleteHero(hero.id).subscribe();
     this.messageService.add(`${hero.name} was deleted`)

  }   

}
