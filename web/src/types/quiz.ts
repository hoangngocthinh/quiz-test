export enum QuestionType {
  MULTIPLE_CHOICE,
  ESSAY
}

export interface Quiz {
  id: string
  name: string
}

export interface SearchQuiz {
  search?: string
}

export interface SearchQuestion {
  quiz_id: string
}


export interface LeaderBoard {
  id: string
  username: string
  score: number
  rank: number
}

export interface Choice {
  id: string
  choice_text: string
  is_correct: false
}

export interface Question {
  id?: string
  quiz: string
  question_text?: string
  type: QuestionType
  choices?: Choice[]
}

export interface Session {
  quiz: string
  start_time: string
  end_time: string
  max_participants: 50
}
