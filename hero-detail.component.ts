import { Component, Input, input, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Hero } from '../heroes/hero';
import { HeroService } from '../hero.service';
import { ActivatedRoute } from '@angular/router';
import { constants } from 'buffer';
import { Location } from '@angular/common';

@Component({
  selector: 'app-hero-detail',
  imports: [CommonModule],
  templateUrl: './hero-detail.component.html',
  styleUrl: './hero-detail.component.css'
})
export class HeroDetailComponent implements OnInit {
@Input () 
hero? : Hero
constructor(private HeroService:HeroService,private route:ActivatedRoute,private location:Location) {
  
}
ngOnInit():void{

this.getHero()
}
  getHero() {
const id=Number(this.route.snapshot.paramMap.get('id'));
this.HeroService.getHero(id).subscribe(x=>this.hero =x);
  }
  goBack():void{
this.location.back();

  }
  save():void{
    if(this.hero)
   this.HeroService.updateHero(this.hero).subscribe();

  }
}
